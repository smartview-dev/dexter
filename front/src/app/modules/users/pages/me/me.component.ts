import { CommonModule } from '@angular/common';
import { Component, inject, OnInit } from '@angular/core';
import { User } from '@users/models/user.model';
import { UsersService } from '@users/services/users.service';

@Component({
  selector: 'app-me',
  imports: [CommonModule],
  templateUrl: './me.component.html',
  styleUrl: './me.component.css',
})
export class MeComponent implements OnInit {
  private userService = inject(UsersService);
  public user: User | null = null;

  ngOnInit() {
    this.userService.user$.subscribe((user) => {
      this.user = user;
    });
  }
}
