import { Component, inject, OnInit } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarComponent } from '../navbar/navbar.component';
import { UsersService } from '@users/services/users.service';
import { User } from '@users/models/user.model';

@Component({
  selector: 'app-layout',
  imports: [RouterModule, NavbarComponent],
  templateUrl: './layout.component.html',
})
export class LayoutComponent implements OnInit {
  private usersService = inject(UsersService);

  ngOnInit() {
    this.usersService.getMe().subscribe();
  }
}
