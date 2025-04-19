import { Component } from '@angular/core';
import { RouterModule } from '@angular/router';
import { NavbarComponent } from '../navbar/navbar.component';

@Component({
  selector: 'app-layout',
  imports: [RouterModule, NavbarComponent],
  templateUrl: './layout.component.html',
})
export class LayoutComponent {}
