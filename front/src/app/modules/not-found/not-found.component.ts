import { NgOptimizedImage } from '@angular/common';
import { Component } from '@angular/core';
import { RouterLinkWithHref } from '@angular/router';

@Component({
  selector: 'app-not-found',
  imports: [RouterLinkWithHref, NgOptimizedImage],
  templateUrl: './not-found.component.html',
  styleUrl: './not-found.component.css',
})
export class NotFoundComponent {
  image404 = 'svg/404.svg';
  imageAlt = 'Not Found Image';
}
