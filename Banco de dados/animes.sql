-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 28/10/2024 às 21:46
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `animes`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `anime`
--

CREATE TABLE `anime` (
  `id` int(11) NOT NULL,
  `nome_personagem` varchar(100) NOT NULL,
  `nome_poder` varchar(100) NOT NULL,
  `valor_ataque` decimal(5,2) NOT NULL,
  `valor_defesa` decimal(5,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `anime`
--

INSERT INTO `anime` (`id`, `nome_personagem`, `nome_poder`, `valor_ataque`, `valor_defesa`) VALUES
(1, 'Naruto', 'Rasengan', 10.00, 5.00),
(2, 'Gohan', 'Masenko', 10.00, 5.00),
(3, 'Kang-Chan', 'Facada', 5.00, 3.00),
(4, 'Hulk', 'Hulk esmaga', 7.00, 20.00),
(5, 'Homem de ferro', 'rajada energética', 6.00, 11.00),
(6, 'Homem aranha', 'rajada de teias', 2.00, 15.00),
(7, 'Vegeta', 'Resplendor final', 12.00, 6.00),
(8, 'Kakashi', 'Kamui', 12.00, 5.00);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `anime`
--
ALTER TABLE `anime`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `anime`
--
ALTER TABLE `anime`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
