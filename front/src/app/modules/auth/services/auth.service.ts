import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from '@env/environment';
import { tap } from 'rxjs';
import { TokenService } from '@shared/services/token.service';
import { ResponseLogin } from '@auth/models/auth.model';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private readonly authEndpoint = `${environment.apiUrl}/v1/auth/login`;

  constructor(
    private http: HttpClient,
    private tokenService: TokenService,
  ) {}

  login(params: { username: string; password: string }) {
    const httpParams = new HttpParams()
      .set('username', params.username)
      .set('password', params.password);
    return this.http
      .post<ResponseLogin>(
        `${this.authEndpoint}?${httpParams.toString()}`,
        null,
      )
      .pipe(
        tap((response: ResponseLogin) => {
          this.tokenService.saveToken(response.token);
        }),
      );
  }

  logout() {
    this.tokenService.removeToken();
  }
}
