export class ScheduledTweet {
  constructor(
    public tweetContent: string,
    public timeToSend: string,
    public userid: string,
    public tweetType: string,
    public threadOrderId: number,
  ) { }
}