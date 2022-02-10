export class ScheduledTweet {
  constructor(
    public tweetContent: string,
    public timeToSend: string,
    public timeSent: string,
    public userId: string,
    public tweetType: string,
    public threadOrderId: number,
    public sent: number,
    public done: number,
    public id: string
  ) { }
}