import { Component } from '@angular/core';
import { CommonModule, NgOptimizedImage } from '@angular/common';

@Component({
  selector: 'app-auth',
  imports: [CommonModule, NgOptimizedImage],
  templateUrl: './auth.component.html',
  styleUrl: './auth.component.css',
})
export class AuthComponent {
  loginImage = 'svg/chatbot.svg';
  loginAlt = 'Chatbot Image';
}
