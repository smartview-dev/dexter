import { Component, computed, input } from '@angular/core';
import {
  AlertTriangle,
  CheckCircle2,
  Info,
  LucideAngularModule,
  XCircle,
} from 'lucide-angular';

type AlertType = 'info' | 'success' | 'warning' | 'error';
type AlertStyle = 'soft' | 'outline' | 'dash';

@Component({
  selector: 'app-alert',
  imports: [LucideAngularModule],
  templateUrl: './alert.component.html',
  styleUrl: './alert.component.css',
})
export class AlertComponent {
  type = input.required<AlertType>();
  variant = input<AlertStyle>();
  message = input.required<string>();
  class = input<string>();

  icon = computed(() => {
    const icons = {
      info: Info,
      success: CheckCircle2,
      warning: AlertTriangle,
      error: XCircle,
    };
    return icons[this.type()];
  });

  alertClass = computed(() => {
    const base = 'alert';
    const typeClass = `alert-${this.type()}`;
    const variantClass = this.variant() ? `alert-${this.variant()}` : '';
    const custom = this.class() || '';

    return `${base} ${typeClass} ${variantClass} ${custom}`;
  });
}
