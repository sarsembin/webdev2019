import {BrowserModule} from '@angular/platform-browser';
import {NgModule, ClassProvider} from '@angular/core';
import {FormsModule} from '@angular/forms';
import {AppComponent} from './app.component';
import {ParentComponent} from './parent/parent.component';
import {ProviderService} from './provider.service';
import {HttpClientModule, HTTP_INTERCEPTORS} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AuthInterceptor } from './AuthInterceptor';

@NgModule({
  declarations: [
    AppComponent,
    ParentComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [
    ProviderService,
    <ClassProvider> {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule {
}