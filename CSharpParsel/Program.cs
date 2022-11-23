using System.Net.Http;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
//using Newtonsoft.Json.Serialization;
// Устанавливаем библиотеку:
// dotnet add package Newtonsoft.Json


string token = File.ReadAllText("token.config");
HttpClient hc = new();
hc.BaseAddress = new Uri($"https://api.telegram.org/bot{token}/");
string contentObj = hc.GetStringAsync("getme").Result;
JObject obj = JObject.Parse(contentObj);
// Здесь мы получаем имя и username бота через команду getme.
System.Console.WriteLine(obj["result"]["first_name"]);
System.Console.WriteLine(obj["result"]["username"]);


// Здесь мы считываем текст у бота.
int offset = 0;
string rawData = hc.GetStringAsync($"getUpdates?offset={offset}").Result;
JObject obj2 = JObject.Parse(rawData);
JArray messages = JArray.Parse(obj2["result"].ToString());
for (int i = 0; i < messages.Count; i++)
{
    Console.Write($"{messages[i]["update_id"]} ");  //Здесь мы смотрим id сообщения.
    Console.Write($"{messages[i]["message"]["from"]["first_name"]}->"); //Здесь мы смотрим от кого сообщения.
    Console.WriteLine($"{messages[i]["message"]["text"]}");//Здесь мы смотрим текст сообщения.
}
System.Console.WriteLine(messages.Count);//Здесь мы смотрим кол-во непрочитанных сообщений.

/*
Вводим в строку браузера:
https://api.telegram.org/bot<Токен бота>/getMe
Получаем:
{
    "ok":true,
    "result":{
        "id":5731423337,"is_bot":true,
        "first_name":"Denis_Super_Bot",
        "username":"Denis_Super_bot",
        "can_join_groups":true,
        "can_read_all_group_messages":false,
        "supports_inline_queries":false}
}
*/