import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LayoutComponent } from './shared/components/layout/layout.component';

const routes: Routes = [
  {
    path: '',
    component: LayoutComponent,
    children: [
      {
        path: 'chat',
        loadComponent: () =>
          import('./chat/pages/index/index.component').then(
            (m) => m.IndexComponent,
          ),
        title: 'Dexter: Chat',
      },
      {
        path: 'config',
        loadChildren: () =>
          import('./config/config.module').then((m) => m.ConfigModule),
        title: 'Dexter: Configuration',
      },
      {
        path: 'users',
        loadChildren: () =>
          import('./users/users.module').then((m) => m.UsersModule),
        title: 'Dexter: Users',
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class ModulesRoutingModule {}
