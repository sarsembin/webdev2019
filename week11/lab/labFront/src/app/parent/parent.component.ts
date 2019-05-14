import {Component, OnDestroy, OnInit} from '@angular/core';
import {ProviderService} from '../provider.service';
import {ICategory, IProduct} from '../modules';

@Component({
  selector: 'app-parent',
  templateUrl: './parent.component.html',
  styleUrls: ['./parent.component.css']
})
export class ParentComponent implements OnInit, OnDestroy {

  public subTitle = '';
  public array2: any[] = [];

  public categories: ICategory[] = [];
  public loading = false;

  public interval;
  public i = 0;

  public products: IProduct[] = [];

  constructor(private provider: ProviderService) { }

  ngOnInit() {

    this.provider.getCategories().then(res => {
      this.categories = res;
      this.loading = true;
    });

  }

  getProducts(category: ICategory) {
    this.provider.getCategoryProducts(category.id).then(res => {
      this.products = res;
    });
  }

  ngOnDestroy() {
    clearInterval(this.interval);
  }

}
