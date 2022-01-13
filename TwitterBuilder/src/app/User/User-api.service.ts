import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { API_URL } from '../env';
import { User } from './User.model';
import { catchError } from 'rxjs/operators';

@Injectable()
export class UsersApiService {

  constructor(private http: HttpClient) {
  }

  _handleError(err: HttpErrorResponse | any) {
    return throwError(err.message || 'Error: Unable to complete request.');
  }

  // GET list of public, future events
  getUsers(searchTerm: string): Observable<User[]> {
    console.log("getting Users")
    return this.http.get<User[]>(`http://127.0.0.1:5000/NicheUsers/${searchTerm}`).pipe(catchError(this._handleError));
  }

  addUserToWatchList(watchListUserId: number, userId: number) :Observable<string> {
    console.log("Sending AddWatchListUser Request")
    let parameters = new HttpParams()
      .set('watchListUserId', watchListUserId)
      .set('userId', userId);
    
    return this.http.get<string>('http://127.0.0.1:5000/AddWatchListUser', { params: parameters }).pipe(catchError(this._handleError));
  }
}

