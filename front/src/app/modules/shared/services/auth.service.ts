import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { environment } from '@env/environment';
import { ResponseLogin } from '../models/auth.model';
import { tap } from 'rxjs';
import { TokenService } from './token.service';

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  private readonly loginEndpoint = `${environment.apiUrl}/v1/users/login`;

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
        `${this.loginEndpoint}?${httpParams.toString()}`,
        null,
      )
      .pipe(
        tap((response: ResponseLogin) => {
          this.tokenService.saveToken(response.token);
        }),
      );
  }
}
