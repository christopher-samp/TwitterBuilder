export class Tweet {
  constructor(
    public data: string,
    public id: string,
    public retweets: number,
    public favorites: number,
    public date: string,
    public profile_image_url_https: string,
    public username: string,
    public userid: string
  ) { }
}