import { Component } from '@angular/core';
import { CommonModule, NgOptimizedImage } from '@angular/common';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';

@Component({
  selector: 'app-auth',
  imports: [CommonModule, NgOptimizedImage, ReactiveFormsModule],
  templateUrl: './auth.component.html',
  styleUrl: './auth.component.css',
})
export class AuthComponent {
  loginImage = 'svg/chatbot.svg';
  loginAlt = 'Chatbot Image';

  form: FormGroup;

  constructor(private formBuilder: FormBuilder) {
    this.form = this.formBuilder.nonNullable.group({
      email: ['', [Validators.email, Validators.required]],
      password: ['', [Validators.required, Validators.minLength(5)]],
    });
  }

  doLogin() {
    // Implement your login logic here
    console.log(this.form.valid);
    if (this.form.valid) {
      const { email, password } = this.form.getRawValue();
      // TODO
      console.log('Login successful', { email, password });
    } else {
      this.form.markAllAsTouched();
    }
    console.log('Login button clicked');
  }
}
