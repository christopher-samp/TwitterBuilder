import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
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
}

