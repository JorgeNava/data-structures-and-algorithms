/* 
1. Amazon Transaction Logs (example question)

Your Amazonian team is responsible for maintaining a monetary transaction service. The transactions are tracked in a log file.

A log file is provided as a string array where each entry represents a transaction to service. Each transaction consists of:

sender_user_id: Unique identifier for the user that initiated the transaction. It consists of only digits with at most 9 digits.
recipient_user_id: Unique identifier for the user that is receiving the transaction. It consists of only digits with at most 9 digits.
amount_of_transaction: The amount of the transaction. It consists of only digits with at most 9 digits.
The values are separated by a space. For example, "sender_user_id recipient_user_id amount_of_transaction".

Users that perform an excessive amount of transactions might be abusing the service so you have been tasked to identify the users that have a number of transactions over a threshold. The list of user ids should be ordered in ascending numeric value.

Example

logs = ["88 99 200", "88 99 300", "99 32 100", "12 12 15"]
threshold = 2
The transactions count for each user, regardless of role are:

ID    Transactions
--    -------------
99    3
88    2
12    1
32    1

There are two users with at least threshold = 2 transactions: 99 and 88. In ascending order, the return array is ['88', '99'].

Note: In the last log entry, user 12 was on both sides of the transaction. This counts as only 1 transaction for user 12.

Function Description

Complete the function processLogs in the editor below.

The function has the following parameter(s):

string logs[n]: the log entries in the logs
int threshold: the minimum number of transactions that a user must have to be included in the result
Returns:

string[]: an array of user id's as strings, sorted ascending by numeric value

*/

let usersTransactions = {};

function processLogs(logs, threshold) {
  const rslt = [];
  logs.forEach(log => {
    const [senderId, recipientId] = log.split(' ');
    if (!usersTransactions.hasOwnProperty(senderId)) {
      usersTransactions[senderId] = 1;
    } else {
      usersTransactions[senderId] += 1;
    }

    if (!usersTransactions.hasOwnProperty(recipientId)) {
      usersTransactions[recipientId] = 1;
    } else {
      if (senderId !== recipientId) {
        usersTransactions[recipientId] += 1;
      }
    }
  });
  for (const userId in usersTransactions) {
    if (usersTransactions[userId] >= threshold) rslt.push(userId);
  }
  return rslt;
}