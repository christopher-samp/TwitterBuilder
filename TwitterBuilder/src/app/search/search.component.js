document.querySelector("#addLinks").addEventListener("keyup", event => {
  if (event.key !== "Enter") return; // Use `.key` instead.
  document.querySelector("#searchTweets").click(); // Things you want to do.
  event.preventDefault(); // No need to `return false;`.
});