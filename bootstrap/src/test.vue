<script>
const axios = require('axios');
const cheerio = require('cheerio');

async function crawlWeatherInfo() {
  const query = 'Jeongwang-dong';
  const searchUrl = `https://search.naver.com/search.naver?query=${encodeURIComponent(query)}`;

  try {
    const response = await axios.get(searchUrl);
    const $ = cheerio.load(response.data);

    const weatherElement = $('.info_weather').first();
    const temperature = weatherElement.find('.todaytemp').text();
    const description = weatherElement.find('.cast_txt').text();

    console.log(`Temperature in Jeongwang-dong: ${temperature}°C`);
    console.log(`Weather description: ${description}`);
  } catch (error) {
    console.error('Error occurred while fetching weather information:', error);
  }
}

crawlWeatherInfo();

</script>