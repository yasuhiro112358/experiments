// db.createUser({
//   user: 'admin',
//   pwd: 'password',
//   roles: [
//     {
//       role: 'readWrite',
//       db: 'mydatabase'
//     }
//   ]
// });

db = db.getSiblingDB('mydatabase');
db.createCollection('mycollection');
