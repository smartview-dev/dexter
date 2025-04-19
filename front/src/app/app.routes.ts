import { Routes } from '@angular/router';
import { NotFoundComponent } from '@modules/not-found/not-found.component';
import { AuthGuard } from '@modules/shared/guards/auth.guard';

export const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: '',
        loadComponent: () =>
          import('./modules/auth/auth.component').then((m) => m.AuthComponent),
      },
      {
        path: '',
        canActivate: [AuthGuard],
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
