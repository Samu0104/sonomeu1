<?php
    if(isset($_POST["submit"]))
    {
        print_r($_POST["nome"]);
        print_r($_POST["data_nasc"]);
        print_r($_POST["email"]);
        print_r($_POST["nomepassword"]);
    }
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SONOMEU</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        * {
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        header{
            width: 100xp;
            height: 300xp;
            font-family: arial;
            color:#9db8d1;
            background-color:#9db8d1;
        }
        #dif{
            text-align:left
        }
        nav{
            width: 10xp;
            height: 5xp;
            background-color:#9db8d1;
            font-size: 3px;
        }
        section{
            text-align: center;
            background:#fbe3e9;
        }
        #links{
            display: grid;
            grid-template-columns: auto auto;
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <img src="./FE13239C-3CBE-41EB-8024-CA7871E3F2F6_L0_001-01_08_2024, 14_40_42.png" width="100" height="100" text-align:right />
    </header>
    <nav>ﾠ</nav>
    <section>
        <div>
            <h1>Cadastrar</h1>
            <form action="cadastrar.php" method = "POST" action="interface.HTML">
                <p>
                    <label for="name">Nome</label>
                    <input
                        type="text"
                        id="name"
                        name="name"
                    />
                </p>
                <p>
                    <label for="data_nasc">Data de Nascimento</label>
                    <input
                        type="date"
                        id="data_nasc"
                        nome="data_nasc"
                    />
                </p>
                <p>
                    <label for="email">Email</label>
                    <input
                        type="text"
                        id="email"
                        nome="email"
                    />
                </p>
                <p>
                    <label for="password">Senha</label>
                    <input
                        type="password"
                        id="password"
                        name="password"
                    />
                </p>
                <input type="submit" value="Enviar" />
            </form>
        </div>
        <div class="links">
            <h5>Já tem uma conta?</h5> <a href="./entrar.html">ENTRAR</a>
        </div>
    </section>
</body>
</html>
