#EXEMPLO SEM APLICAR LEI DE DEMETER
public class ServicoDeImpressao {
    public void imprimirDadosDaPessoa(Pessoa pessoa) {
        
        String nomeCidade = pessoa.getEndereco().getCidade().getNome();

        System.out.println("Nome: " + pessoa.getNome());
        System.out.println("Cidade: " + nomeCidade);
        System.out.println("CPF: " + pessoa.getCpf());
        }
}
#APLICANDO LEI DE DEMETER
public class ServicoDeImpressao {
    public void imprimirDadosDaPessoa(Pessoa pessoa){
        String nomeCidade = pessoa.getCidade();

        System.out.println("Nome: " + pessoa.getNome());
        System.out.println("Cidade: " + nomeCidade);
        System.out.println("CPF: " + pessoa.getCpf());
    }
}