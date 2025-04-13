import { Routes } from '@angular/router';
import { NotFoundComponent } from '@modules/not-found/not-found.component';
import { LayoutComponent } from '@modules/shared/components/layout/layout.component';

export const routes: Routes = [
  {
    path: '',
    component: LayoutComponent,
    children: [
      {
        path: '',
        loadComponent: () =>
          import('./modules/auth/auth.component').then((m) => m.AuthComponent),
      },
    ],
  },
  {
    path: '**',
    component: NotFoundComponent,
  },
];
