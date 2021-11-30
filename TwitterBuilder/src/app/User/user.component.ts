import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { UsersApiService } from './User-api.service'
import { User } from './User.model'

@Component({
  templateUrl: './user.component.html',
})
export class UsersComponent implements OnInit, OnDestroy {
  title = 'TwitterBuilder';

  UserListSubs: Subscription;
  UserList: User[];

  constructor(private usersApi: UsersApiService) {
    console.log("app component constructor")
  }

  ngOnInit() {
    console.log("init NG")

    this.UserListSubs = this.usersApi
      .getUsers()
      .subscribe(res => {
        this.UserList = res;
      },
        console.error
      );

  }

  ngOnDestroy() {
    this.UserListSubs.unsubscribe();
  }
}
