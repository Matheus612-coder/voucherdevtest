-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 18/10/2024 às 22:37
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `Sistema_de_vendas`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `Cliente`
--

CREATE TABLE `Cliente` (
  `id_cliente` int(11) NOT NULL,
  `nome` char(100) NOT NULL,
  `cpf` int(11) NOT NULL,
  `telefone` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `Cliente`
--

INSERT INTO `Cliente` (`id_cliente`, `nome`, `cpf`, `telefone`) VALUES
(1, 'Ana', 1234567890, 9900112),
(2, 'João', 1234567890, 99001123);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Produto`
--

CREATE TABLE `Produto` (
  `id_produto` int(11) NOT NULL,
  `nome` char(100) NOT NULL,
  `preco` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `Produto`
--

INSERT INTO `Produto` (`id_produto`, `nome`, `preco`) VALUES
(1, 'camiseta', 49),
(2, 'Sapato', 100);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Venda`
--

CREATE TABLE `Venda` (
  `id_venda` int(11) NOT NULL,
  `data_venda` date NOT NULL,
  `id_cliente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `Venda`
--

INSERT INTO `Venda` (`id_venda`, `data_venda`, `id_cliente`) VALUES
(3, '2024-10-18', 1),
(4, '0000-00-00', 2);

-- --------------------------------------------------------

--
-- Estrutura para tabela `Venda_produto`
--

CREATE TABLE `Venda_produto` (
  `idVenda_produto` int(11) NOT NULL,
  `id_venda` int(11) DEFAULT NULL,
  `id_produto` int(11) DEFAULT NULL,
  `quantidade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `Venda_produto`
--

INSERT INTO `Venda_produto` (`idVenda_produto`, `id_venda`, `id_produto`, `quantidade`) VALUES
(1, 3, 1, 4),
(2, 4, 2, 5);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `Cliente`
--
ALTER TABLE `Cliente`
  ADD PRIMARY KEY (`id_cliente`);

--
-- Índices de tabela `Produto`
--
ALTER TABLE `Produto`
  ADD PRIMARY KEY (`id_produto`);

--
-- Índices de tabela `Venda`
--
ALTER TABLE `Venda`
  ADD PRIMARY KEY (`id_venda`),
  ADD KEY `id_cliente` (`id_cliente`);

--
-- Índices de tabela `Venda_produto`
--
ALTER TABLE `Venda_produto`
  ADD PRIMARY KEY (`idVenda_produto`),
  ADD KEY `id_venda` (`id_venda`),
  ADD KEY `id_produto` (`id_produto`);

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `Venda`
--
ALTER TABLE `Venda`
  ADD CONSTRAINT `Venda_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `Cliente` (`id_cliente`);

--
-- Restrições para tabelas `Venda_produto`
--
ALTER TABLE `Venda_produto`
  ADD CONSTRAINT `Venda_produto_ibfk_1` FOREIGN KEY (`id_venda`) REFERENCES `Venda` (`id_venda`),
  ADD CONSTRAINT `Venda_produto_ibfk_2` FOREIGN KEY (`id_produto`) REFERENCES `Produto` (`id_produto`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
