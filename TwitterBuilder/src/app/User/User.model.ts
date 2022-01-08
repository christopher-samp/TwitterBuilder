export class User {
  constructor(
    public username: string,
    public userid: number,
    public usernameAt: string,
    public followers: number,
    public following: number,
    public statuses_count: number,
    public profile_image_url_https: string,
    public profile_banner_url: string,
    public description: string
  ) { }
}