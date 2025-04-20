import { CommonModule, NgClass, NgIf } from '@angular/common';
import { Component, input } from '@angular/core';
import { RequestStatus } from '@modules/shared/models/request-status.model';

type ChatType = 'end' | 'start';

@Component({
  selector: 'app-chat-view',
  imports: [CommonModule, NgIf, NgClass],
  standalone: true,
  templateUrl: './chat-view.component.html',
  styleUrl: './chat-view.component.css',
})
export class ChatViewComponent {
  class = input<string>();
  message = input.required<string>();
  requestStatus = input.required<RequestStatus>();
  type = input.required<ChatType>();
}
