import redis from 'redis';
// task 2 - implement async
import { promisify } from 'util';

const client = redis.createClient();
const addAsync = promisify(client.get).bing(client);

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Task 1
function setNewSchool (schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, (err, res) => {
    console.log(res);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
