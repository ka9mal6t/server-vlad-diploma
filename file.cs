using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text.Json;
using System.Threading.Tasks;

namespace FastAPI_Console_Client
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var httpClient = new HttpClient();
            httpClient.BaseAddress = new Uri("http://localhost:8000"); // Замените на ваш URL FastAPI

            // Регистрация пользователя


            var registerResponse = await httpClient.PostAsync("/auth/register", registerContent);
            if (registerResponse.IsSuccessStatusCode)
            {
                Console.WriteLine("Пользователь успешно зарегистрирован.");
            }
            else
            {
                Console.WriteLine("Ошибка при регистрации пользователя.");
                return;
            }

            // Логин пользователя
            var loginData = new
            {
                username = "testuser",
                password = "testpassword"
            };

            var loginContent = new StringContent(
                JsonSerializer.Serialize(loginData),
                System.Text.Encoding.UTF8,
                "application/json"
            );

            var loginResponse = await httpClient.PostAsync("/auth/login", loginContent);
            if (loginResponse.IsSuccessStatusCode)
            {
                var accessToken = await loginResponse.Content.ReadAsStringAsync();
                Console.WriteLine("Пользователь успешно вошел в систему. Токен доступа: " + accessToken);

                // Получение информации о текущем пользователе
                var infoRequest = new HttpRequestMessage(HttpMethod.Get, "/auth/info");
                // Копирование куки из ответа на запрос логина
                foreach (var cookie in loginResponse.Headers.GetValues("Set-Cookie"))
                {
                    httpClient.DefaultRequestHeaders.Add("Cookie", cookie);
                }

                var infoResponse = await httpClient.SendAsync(infoRequest);
                if (infoResponse.IsSuccessStatusCode)
                {
                    var userInfoJson = await infoResponse.Content.ReadAsStringAsync();
                    var userInfo = JsonSerializer.Deserialize<SUserInfo>(userInfoJson);
                    Console.WriteLine("Информация о текущем пользователе:");
                    Console.WriteLine($"Имя пользователя: {userInfo.username}");
                    // Дополнительная информация о пользователе, если она доступна
                }
                else
                {
                    Console.WriteLine("Ошибка при получении информации о пользователе.");
                }

                // Запрос на добавление друга


            var loginData = new
            {
                username = "testuser",
            };

            var loginContent = new StringContent(
                JsonSerializer.Serialize(loginData),
                System.Text.Encoding.UTF8,
                "application/json"
            );

            var loginResponse = await httpClient.PostAsync("/friends/add_friend", loginContent);
            if (loginResponse.IsSuccessStatusCode)
            {
                Console.WriteLine("Друг успешно добавлен.");
            }






            var loginResponse = await httpClient.GetAsync("/friends/get_friends");
            if (loginResponse.IsSuccessStatusCode)
            {

                var usersInfoJson = await infoResponse.Content.ReadAsStringAsync();
                var userInfo = JsonSerializer.Deserialize<List<SFriendUserInfo>>(userInfoJson);
                foreach(var user in userInfo)
                {
                    Console.WriteLine($"Имя пользователя: {user.username}");
                    Console.WriteLine($"Код пользователя: {user.code}");
                }
            }





                // Логаут пользователя
                var logoutResponse = await httpClient.PostAsync("/auth/logout", null);
                if (logoutResponse.IsSuccessStatusCode)
                {
                    Console.WriteLine("Пользователь успешно вышел из системы.");
                }
                else
                {
                    Console.WriteLine("Ошибка при выходе пользователя из системы.");
                }
            }
            else
            {
                Console.WriteLine("Ошибка при входе пользователя.");
            }
        }
    }

    public class SUserInfo
    {
        public string username { get; set; }
        public string code { get; set; }
        public int count_changes { get; set; }

        // Дополнительные свойства, если они доступны
    }

    public class SFriendUserInfo
    {
        public string username { get; set; }
        public string code { get; set; }
        // Дополнительные свойства, если они доступны
    }
}