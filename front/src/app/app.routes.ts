import { Routes } from '@angular/router';
import { NotFoundComponent } from '@modules/not-found/not-found.component';
import { authGuard } from '@modules/shared/guards/auth.guard';
import { redirectGuard } from '@modules/shared/guards/redirect.guard';

export const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: '',
        canActivate: [redirectGuard],
        loadComponent: () =>
          import('./modules/auth/auth.component').then((m) => m.AuthComponent),
      },
      {
        path: '',
        canActivate: [authGuard],
        loadChildren: () =>
          import('./modules/modules.module').then((m) => m.ModulesModule),
      },
    ],
  },
  {
    path: '**',
    component: NotFoundComponent,
  },
];
