import { CommonModule } from '@angular/common';
import { Component, inject } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { AuthService } from '@auth/services/auth.service';
import { UsersService } from '@users/services/users.service';

@Component({
  selector: 'app-navbar',
  imports: [RouterModule, CommonModule],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.css',
})
export class NavbarComponent {
  private authService = inject(AuthService);
  private router = inject(Router);
  private usersService = inject(UsersService);
  public user$ = this.usersService.user$;

  logout(event: Event) {
    event.preventDefault();
    this.authService.logout();
    this.router.navigate(['/']);
  }
}
