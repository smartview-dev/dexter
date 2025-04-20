import { Routes } from '@angular/router';
import { authGuard } from '@auth/guards/auth.guard';
import { NotFoundComponent } from '@shared/components/not-found/not-found.component';
import { redirectGuard } from '@shared/guards/redirect.guard';

export const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: '',
        canActivate: [redirectGuard],
        loadComponent: () =>
          import('./modules/auth/pages/auth.component').then(
            (m) => m.AuthComponent,
          ),
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
