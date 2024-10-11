Rode o script 1, 2 e 3, após rodar esses scripts, voce terá os clones achados pelo Siamese.

Entretanto, os nomes "blocos" que chamo são independentes para cada revision, ou seja, o block_0
na review 1000 revision 1 pode ser diferente do block_0 na review 1000 revision 2, se quiser 
fazer um estudo mais apronfundado dos clones e até onde eles irão em cada review, execute os scripts extra em ordem.

Por fim, cheque a primeira ocorrência do bloco que queira analisar, se você for checar o arquivo
platform.ui talvez um nome de um bloco tenha sido renomeado, ou seja, o bloco "workbench_8" na rev 2 pode
ser igual ao "workbench_9" da rev 3, isso fará com que no arquivo, na rev 3, onde tinha workbench_9 terá workbench_8,
isso poderá gerar confusão em ver qual o bloco é o correto, para evitar isso olhe o bloco workbench_8 na rev 2 (caso teste).

Obs: Para rodar o 3° script, o elasticsearch precisa estar rodando e o Siamese configurado
