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
  UserListLeft: User[];
  UserListRight: User[];

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
            this.UserListLeft = res.slice(0, res.length / 2);
            this.UserListRight = res.slice(res.length / 2, res.length);
          },
            console.error
          );
      }
    })
  }

  addToWatchList(watchListUserId: number, userId: number) {
    this.usersApi.addUserToWatchList(watchListUserId, userId).subscribe();
  }

  ngOnDestroy() {
    this.UserListSubs.unsubscribe();
  }
}
