// Strategy Pattern

// possíveis casos de uso:
// ordenação de listas
// renderização gráfica
// validação de dados
// geração de relatórios
// compressão de dados
// algoritmos de busca
// autenticação em sistemas
// simulação de jogos
// processamento de imagens
// gerenciamento de cache

// * Payment
// interface
interface PaymentStrategy {
  processPayment(amount: number): void;
}

// classes
class CreditCardPayment implements PaymentStrategy {
  constructor() {}

  processPayment(amount: number): void {
    console.log("Pagamento de Cartão de Crédito processado: ", amount);
  }
}

class BoletoPayment implements PaymentStrategy {
  constructor() {}

  processPayment(amount: number): void {
    console.log("Pagamento de Boleto processado: ", amount);
  }
}

class DigitalWalletPayment implements PaymentStrategy {
  constructor() {}

  processPayment(amount: number): void {
    console.log("Pagamente de DigitalWallet processado: ", amount);
  }
}

// context
class PaymentContext {
  private paymentStrategy: PaymentStrategy;

  setPaymentStrategy(strategy: PaymentStrategy): void {
    this.paymentStrategy = strategy;
  }

  excutePayment(amount: number): void {
    this.paymentStrategy.processPayment(amount);
  }
}

class OnLineStore {
  private paymentContext: PaymentContext = new PaymentContext();

  processOnLinePurchase(
    amount: number,
    paymentStrategy: PaymentStrategy
  ): void {
    this.paymentContext.setPaymentStrategy(paymentStrategy);
    this.paymentContext.excutePayment(amount);
  }
}

// usage
const onLineStore = new OnLineStore();

const creditCardPayment = new CreditCardPayment();
const boletoPayment = new BoletoPayment();
const digitalWalletPayment = new DigitalWalletPayment();

onLineStore.processOnLinePurchase(72.12, creditCardPayment);
onLineStore.processOnLinePurchase(130.12, boletoPayment);
onLineStore.processOnLinePurchase(149.99, digitalWalletPayment);

// * Auth
interface User {
  email: string;
  password: string;
}

// strategy
interface AuthStrategy {
  authenticate(user: User): void;
}

class GoogleAuthStrategy implements AuthStrategy {
  authenticate(user: User) {
    console.log(`Google Auth authenticated user: ${user.email}`);
  }
}

class GitHubAuthStrategy implements AuthStrategy {
  authenticate(user: User) {
    console.log(`GitHub Auth authenticated user: ${user.email}`);
  }
}

class FacebookAuthStrategy implements AuthStrategy {
  authenticate(user: User) {
    console.log(`Facebook Auth authenticated user: ${user.email}`);
  }
}

// context
class AuthContext {
  private authStrategy: AuthStrategy;

  setAuthStrategy(authStrategy: AuthStrategy) {
    this.authStrategy = authStrategy;
  }

  executeAuth(user: User) {
    this.authStrategy.authenticate(user);
  }
}

class Login {
  private authContext: AuthContext = new AuthContext();

  authenticateUser(user: User, authStrategy: AuthStrategy): void {
    this.authContext.setAuthStrategy(authStrategy);
    this.authContext.executeAuth(user);
  }
}

// implementation
const login = new Login();

const googleAuth = new GoogleAuthStrategy();
const gitHubAuth = new GitHubAuthStrategy();
const facebookAuth = new FacebookAuthStrategy();

const user = { email: "user@email.com", password: "password" };

login.authenticateUser(user, googleAuth);
login.authenticateUser(user, gitHubAuth);
login.authenticateUser(user, facebookAuth);
