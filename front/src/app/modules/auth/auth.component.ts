import { Component, inject, signal } from '@angular/core';
import { NgIf, NgOptimizedImage } from '@angular/common';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { AuthService } from '@modules/shared/services/auth.service';
import { RequestStatus } from '@modules/shared/models/request-status.model';
import { AlertComponent } from '@modules/shared/components/alert/alert.component';
import { Router } from '@angular/router';

@Component({
  selector: 'app-auth',
  standalone: true,
  imports: [NgOptimizedImage, ReactiveFormsModule, NgIf, AlertComponent],
  templateUrl: './auth.component.html',
})
export class AuthComponent {
  readonly loginImage = 'svg/chatbot_2.svg';
  readonly loginAlt = 'Chatbot Image';

  private fb = inject(FormBuilder);
  form = this.fb.nonNullable.group({
    email: ['', [Validators.email, Validators.required]],
    password: ['', [Validators.required, Validators.minLength(5)]],
  });

  status = signal<RequestStatus>('init');
  private authService = inject(AuthService);
  private router = inject(Router);

  async doLogin() {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }

    this.status.set('loading');
    const { email, password } = this.form.getRawValue();

    this.authService.login({ username: email, password }).subscribe({
      next: () => {
        this.status.set('success');
        this.router.navigate(['chat']);
      },
      error: () => {
        this.status.set('failed');
        this.form.controls.password.setValue('');
      },
    });
  }
}
