import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from '@env/environment';
import { TokenService } from '@shared/services/token.service';
import { User } from '@users/models/user.model';
import { BehaviorSubject, tap } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class UsersService {
  private readonly loginEndpoint = `${environment.apiUrl}/v1/users`;
  user$ = new BehaviorSubject<User | null>(null);

  constructor(
    private http: HttpClient,
    private tokenService: TokenService,
  ) {}

  getMe() {
    return this.http
      .get<User>(`${this.loginEndpoint}/me`, {
        headers: {
          Authorization: `Bearer ${this.tokenService.getToken()}`,
        },
      })
      .pipe(
        tap((user) => {
          this.user$.next(user);
        }),
      );
  }
}
