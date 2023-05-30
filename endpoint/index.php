<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <u><h2>PHP simple API by DanielBeeh</h2></u>
    <h2>Manual</h2></br>
    <h4>1. Create endpoint</h4>
    to create endpoint, open the 'simpleapimenu.exe', then choose option 1 to create endpoint. 
    if you prefer to create it manually then simply create files on root_dir/endpoint, naming will be used as url path. 
    for example, if you want to make file that responding to url : 'HOST/listuser' then simply create file 'listuser.php' on endpoint DIRECTORY_SEPARATOR
    on file name, replace / with - example : URL: HOST/list/phone then filename will be 'list-phone.php'
    <h4>2. Query Result to JSON</h4>
    <h4>3. Inserting Data</h4>
    <h4>4. Deleting Data</h4>
    <h4>5. updating Data</h4>
    <h4>6. create token based on user ID</h4>
    <h4>7. login system</h4>
    with login system, you can create level based token. this token can used to identify role of that token so you can allow certain endpoint, function, etc. to use this, u must have field 'role' on your login table, setup table name on './src/api/simpleapi.php'</br>
    how to use : </br>
    use login(USERID,PASS) method, this will generate json with token filed in it if result is not null
    <h4>8. Level Based token</h4>
    <h4>9. Securing endpoint</h4>
</body>
</html>