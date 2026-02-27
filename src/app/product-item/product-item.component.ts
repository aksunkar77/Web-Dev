import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../models/product.model';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css'],
})
export class ProductItemComponent {
  @Input() product!: Product;

  get discountPercent(): number | null {
    if (!this.product?.oldPrice) return null;
    const diff = this.product.oldPrice - this.product.price;
    const p = Math.round((diff / this.product.oldPrice) * 100);
    return p > 0 ? p : null;
  }

  openLink() {
    if (this.product?.link) window.open(this.product.link, '_blank');
  }

  formatMoney(x: number): string {
    
    const s = Math.round(x).toString();
    return s.replace(/\B(?=(\d{3})+(?!\d))/g, ' ') + ' ₸';
  }
}