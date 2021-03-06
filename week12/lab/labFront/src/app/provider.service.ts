import {Injectable} from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {ICategory, IProduct, IAuth} from './modules';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  getCategories(): Promise<ICategory[]> {
    return this.get('http://localhost:8000/tasklists/', {});
  }

  getCategoryProducts(id: number): Promise<IProduct[]> {
    return this.get(`http://localhost:8000/tasklists/${id}/tasks/`, {});
  }

  auth(login: string, password: string): Promise<IAuth> {
    return this.post('http://localhost:8000/login/', {
      username: login,
      password: password
    });
  }
}