export class User {
  constructor(
    public name: string,
    public id: number,
    public screen_name: string,
    public followers_count: number,
    public friends_count: number,
    public statuses_count: number,
    public profile_image_url_https: string
  ) { }
}