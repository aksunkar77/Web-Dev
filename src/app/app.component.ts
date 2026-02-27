import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { ProductService } from './services/product.service';
import { ProductListComponent } from './product-list/product-list.component';

import { Category } from './models/category.model';
import { Product } from './models/product.model';

type SortKey = 'popular' | 'price_asc' | 'price_desc' | 'rating';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule, ProductListComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {

  categories: Category[] = [];
  products: Product[] = [];

  activeTopTab: 'shop' | 'scooter' = 'shop';
  selectedCategoryId = 1;

  query = '';
  sort: SortKey = 'popular';

  priceRanges = [
    { label: 'Up to 10,000 ₸', min: 0, max: 10000 },
    { label: '10,000 – 49,999 ₸', min: 10000, max: 49999 },
    { label: '50,000 – 99,999 ₸', min: 50000, max: 99999 },
    { label: '100,000 – 149,999 ₸', min: 100000, max: 149999 },
    { label: '150,000 – 199,999 ₸', min: 150000, max: 199999 },
    { label: '200,000 – 499,999 ₸', min: 200000, max: 499999 },
    { label: '500,000 ₸ and above', min: 500000, max: Infinity },
  ];

  selectedRanges = new Set<number>();

  constructor(private ps: ProductService) {
    this.categories = ps.getCategories();
    this.products = ps.getProducts();
  }

  setTab(tab: 'shop' | 'scooter') {
    this.activeTopTab = tab;
  }

  selectCategory(id: number) {
    this.selectedCategoryId = id;
    this.query = '';
    this.selectedRanges.clear();
    this.sort = 'popular';
  }

  toggleRange(i: number) {
    if (this.selectedRanges.has(i)) {
      this.selectedRanges.delete(i);
    } else {
      this.selectedRanges.add(i);
    }
  }

  get currentCategoryName(): string {
    return this.categories.find(c => c.id === this.selectedCategoryId)?.name ?? '';
  }

  get filteredProducts(): Product[] {

    let list = this.products.filter(
      p => p.categoryId === this.selectedCategoryId
    );

    const q = this.query.trim().toLowerCase();

    if (q) {
      list = list.filter(p =>
        p.name.toLowerCase().includes(q)
      );
    }

    if (this.selectedRanges.size > 0) {
      list = list.filter(p => {

        for (const idx of this.selectedRanges) {
          const r = this.priceRanges[idx];

          if (p.price >= r.min && p.price <= r.max) {
            return true;
          }
        }

        return false;
      });
    }

    list = [...list];

    if (this.sort === 'price_asc') {
      list.sort((a, b) => a.price - b.price);
    }

    if (this.sort === 'price_desc') {
      list.sort((a, b) => b.price - a.price);
    }

    if (this.sort === 'rating') {
      list.sort((a, b) => b.rating - a.rating);
    }

    return list;
  }
}