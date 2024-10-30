-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Tempo de geração: 18/10/2024 às 23:12
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
-- Banco de dados: `Hotel`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `hospede`
--

CREATE TABLE `hospede` (
  `id_hospede` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `cpf` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `hospede`
--

INSERT INTO `hospede` (`id_hospede`, `nome`, `cpf`) VALUES
(1, 'Carlos Pereira', 1234567891),
(3, 'Ana da Silva', 234567890);

-- --------------------------------------------------------

--
-- Estrutura para tabela `quarto`
--

CREATE TABLE `quarto` (
  `id_quarto` int(11) NOT NULL,
  `tipo_quarto` varchar(70) NOT NULL,
  `preco_diaria` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `quarto`
--

INSERT INTO `quarto` (`id_quarto`, `tipo_quarto`, `preco_diaria`) VALUES
(1, 'suite luxo', 350),
(2, 'quarto padrão', 100);

-- --------------------------------------------------------

--
-- Estrutura para tabela `reserva`
--

CREATE TABLE `reserva` (
  `id_reserva` int(11) NOT NULL,
  `data_inicio` date NOT NULL,
  `data_fim` date NOT NULL,
  `id_quarto` int(11) DEFAULT NULL,
  `id_hospede` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `reserva`
--

INSERT INTO `reserva` (`id_reserva`, `data_inicio`, `data_fim`, `id_quarto`, `id_hospede`) VALUES
(2, '2021-10-12', '2021-10-15', 1, 3),
(4, '2021-10-12', '2021-11-15', 2, 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `hospede`
--
ALTER TABLE `hospede`
  ADD PRIMARY KEY (`id_hospede`);

--
-- Índices de tabela `quarto`
--
ALTER TABLE `quarto`
  ADD PRIMARY KEY (`id_quarto`);

--
-- Índices de tabela `reserva`
--
ALTER TABLE `reserva`
  ADD PRIMARY KEY (`id_reserva`),
  ADD KEY `id_quarto` (`id_quarto`),
  ADD KEY `id_hospede` (`id_hospede`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `hospede`
--
ALTER TABLE `hospede`
  MODIFY `id_hospede` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de tabela `quarto`
--
ALTER TABLE `quarto`
  MODIFY `id_quarto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `reserva`
--
ALTER TABLE `reserva`
  MODIFY `id_reserva` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `reserva`
--
ALTER TABLE `reserva`
  ADD CONSTRAINT `reserva_ibfk_1` FOREIGN KEY (`id_quarto`) REFERENCES `quarto` (`id_quarto`),
  ADD CONSTRAINT `reserva_ibfk_2` FOREIGN KEY (`id_hospede`) REFERENCES `hospede` (`id_hospede`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
