import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.sass']
})
export class SearchComponent implements OnInit {

  searchTerm: String = "";
  constructor(private route: ActivatedRoute, private router: Router) { }

  ngOnInit(): void {
    this.route.params.subscribe(params => {
      if (params['searchTerm'])
        this.searchTerm = params['searchTerm'];
      else
        this.searchTerm = "";
    })
  }

  search(): void {
    console.log(this.searchTerm)
    console.log(location.pathname);
    var baseUrl = location.pathname.split("/")[1];
    if (this.searchTerm)
      this.router.navigate(['/', baseUrl, this.searchTerm]);
    else
      this.searchTerm=""
      // this.router.navigateByUrl("/Tweets/" + this.searchTerm);
  }

}
