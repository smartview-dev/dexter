import { Component } from '@angular/core';
import { ChatViewComponent } from '@chat/components/chat-view/chat-view.component';
import { CircleArrowUp, LucideAngularModule } from 'lucide-angular';

@Component({
  selector: 'app-index',
  templateUrl: './index.component.html',
  imports: [ChatViewComponent, LucideAngularModule],
})
export class IndexComponent {
  readonly icon = CircleArrowUp;
}
