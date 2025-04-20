import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { TokenService } from '@shared/services/token.service';

export const authGuard: CanActivateFn = () => {
  const token = inject(TokenService).getToken();
  const router = inject(Router);

  if (!token) {
    router.navigate(['/']);
    return false;
  }
  return true;
};
