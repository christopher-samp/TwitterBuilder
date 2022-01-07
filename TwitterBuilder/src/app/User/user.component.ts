import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';
import { UsersApiService } from './User-api.service'
import { User } from './User.model'
import { ActivatedRoute } from '@angular/router';

@Component({
  templateUrl: './user.component.html',
})
export class UsersComponent implements OnInit, OnDestroy {
  title = 'TwitterBuilder';

  UserListSubs: Subscription = new Subscription();;
  UserList: User[];

  constructor(private usersApi: UsersApiService, private route: ActivatedRoute) {
    console.log("app component constructor")
  }

  ngOnInit() {
    console.log("init NG")
    this.route.params.subscribe(params => {
      if (params['searchTerm']) {
        this.UserListSubs = this.usersApi
          .getUsers(params['searchTerm'])
          .subscribe(res => {
            this.UserList = res;
          },
            console.error
          );
      }
    })
  }

  ngOnDestroy() {
    this.UserListSubs.unsubscribe();
  }
}
