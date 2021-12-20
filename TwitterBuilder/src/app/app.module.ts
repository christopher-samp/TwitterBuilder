import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TweetsApiService } from './Tweet/Tweet-api.service';
import { UsersApiService } from './User/User-api.service';
import { TweetsComponent } from './Tweet/tweet.component';
import { UsersComponent } from './User/user.component';
import { SearchComponent } from './search/search.component';

@NgModule({
  declarations: [
    AppComponent,
    TweetsComponent,
    UsersComponent,
    SearchComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [TweetsApiService, UsersApiService],
  bootstrap: [AppComponent, TweetsComponent, UsersComponent]
})
export class AppModule { }
