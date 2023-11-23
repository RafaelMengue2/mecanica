from django.db import models

class Cliente(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    codigo = models.AutoField(primary_key=True)
    placa = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.placa

class Mecanico(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.TextField()
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Peca(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class OrdemServico(models.Model):
    numero = models.AutoField(primary_key=True)
    data_emissao = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_conclusao = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(Servico)
    pecas = models.ManyToManyField(Peca)

    def __str__(self):
        return f"OS-{self.numero}"

