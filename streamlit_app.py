<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditor de Faturamento Inteligente</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        .sidebar {
            }
        .sidebar.collapsed {
            width: px;
        }
        .sidebar.collapsed .sidebar-text {
            display: none;
        }
        .sidebar.collapsed .sidebar-icon {
            margin-right: 0;
        }
        .main-content {
            transition: all ease;
        }
        .sidebar.collapsed + .main-content {
            margin-left: px;
        }
        .chart-container {
            height: ;
        }
        .file-upload {
            border:  dashed #cbd5e0;
            transition: all ease;
        }
        .file-upload:hover {
            border-color: #4f46e5;
        }
        .file-upload.dragover {
            border-color: #4f46e5;
            background-color: #eef2ff;
        }
        .inconsistency-badge {
            font-size: ;
            padding: ;
            border-radius: ;
        }
        .badge-error {
            background-color: #fee2e2;
            color: #b91c1c;
        }
        .badge-warning {
            background-color: #fef3c7;
            color: #92400e;
        }
        .badge-success {
            background-color: #d1fae5;
            color: #065f46;
        }
        .badge-info {
            background-color: #e0f2fe;
            color: #0369a1;
        }
        .badge-neutral {
            background-color: #f3f4f6;
            color: #4b5563;
        }
        @media (max-width: ) {
            .sidebar {
                position: fixed;
                z-index: 50;
                transform: translateX(-100%);
            }
            .sidebar.open {
                transform: translateX(0);
            }
            .sidebar.collapsed {
                transform: translateX(-100%);
            }
            .sidebar-toggle {
                display: block;
            }
        }
    </style>
</head>
<body class="bg-gray-50">
    <div class="flex h-screen overflow-hidden">
        <!-- Sidebar -->
        <div class="sidebar bg-white text-gray-800 shadow-md w-64 flex-shrink-0 flex flex-col">
            <div class="p-4 flex items-center justify-between border-b">
                <div class="flex items-center">
                    <i class="fas fa-clinic-medical text-indigo-600 text-2xl sidebar-icon"></i>
                    <span class="ml-2 font-bold text-xl sidebar-text">Auditor Financeiro</span>
                </div>
                <button id="sidebarCollapse" class="text-gray-500 hover:text-gray-700">
                    <i class="fas fa-chevron-left"></i>
                </button>
            </div>
            <div class="flex-1 overflow-y-auto">
                <nav class="p-4">
                    <div class="mb-4">
                        <div class="text-xs uppercase font-semibold text-gray-500 mb-2 sidebar-text">Menu Principal</div>
                        <ul>
                            <li class="mb-1">
                                <a href="#" class="flex items-center p-2 rounded-lg bg-indigo-50 text-indigo-700">
                                    <i class="fas fa-tachometer-alt sidebar-icon mr-3"></i>
                                    <span class="sidebar-text">Dashboard</span>
                                </a>
                            </li>
                            <li class="mb-1">
                                <a href="#" class="flex items-center p-2 rounded-lg hover:bg-gray-100">
                                    <i class="fas fa-file-upload sidebar-icon mr-3"></i>
                                    <span class="sidebar-text">Importar Dados</span>
                                </a>
                            </li>
                            <li class="mb-1">
                                <a href="#" class="flex items-center p-2 rounded-lg hover:bg-gray-100">
                                    <i class="fas fa-search-dollar sidebar-icon mr-3"></i>
                                    <span class="sidebar-text">Auditoria</span>
                                </a>
                            </li>
                            <li class="mb-1">
                                <a href="#" class="flex items-center p-2 rounded-lg hover:bg-gray-100">
                                    <i class="fas fa-file-excel sidebar-icon mr-3"></i>
                                    <span class="sidebar-text">Relatórios</span>
                                </a>
                            </li>
                            <li class="mb-1">
                                <a href="#" class="flex items-center p-2 rounded-lg hover:bg-gray-100">
                                    <i class="fas fa-users sidebar-icon mr-3"></i>
                                    <span class="sidebar-text">Pacientes</span>
                                </a>
                            </li>
                            <li class="mb-1">
                                <a href="#" class="flex items-center p-2 rounded-lg hover:bg-gray-100">
                                    <i class="fas fa-hand-holding-usd sidebar-icon mr-3"></i>
                                    <span class="sidebar-text">Convênios</span>
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div class="mb-4">
                        <div class="text-xs uppercase font-semibold text-gray-500 mb-2 sidebar-text">Configurações</div>
                        <ul>
                            <li class="mb-1">
                                <a href="#" class="flex items-center p-2 rounded-lg hover:bg-gray-100">
                                    <i class="fas fa-cog sidebar-icon mr-3"></i>
                                    <span class="sidebar-text">Configurações</span>
                                </a>
                            </li>
                            <li class="mb-1">
                                <a href="#" class="flex items-center p-2 rounded-lg hover:bg-gray-100">
                                    <i class="fas fa-user-shield sidebar-icon mr-3"></i>
                                    <span class="sidebar-text">Permissões</span>
                                </a>
                            </li>
                            <li class="mb-1">
                                <a href="#" class="flex items-center p-2 rounded-lg hover:bg-gray-100">
                                    <i class="fas fa-question-circle sidebar-icon mr-3"></i>
                                    <span class="sidebar-text">Ajuda</span>
                                </a>
                            </li>
                        </ul>
                    </div>
                </nav>
            </div>
            <div class="p-4 border-t">
                <div class="flex items-center">
                    <img src="https://ui-avatars.com/api/?name=Admin&background=4f46e5&color=fff" alt="User" class="w-8 h-8 rounded-full">
                    <div class="ml-2 sidebar-text">
                        <div class="text-sm font-medium">Administrador</div>
                        <div class="text-xs text-gray-500">admin@clinica.com</div>
                    </div>
                </div>
            </div>
        </div>

        <!-- Main Content -->
        <div class="main-content flex-1 flex flex-col overflow-hidden ml-64">
            <!-- Top Navigation -->
            <header class="bg-white shadow-sm">
                <div class="flex items-center justify-between px-6 py-4">
                    <div class="flex items-center">
                        <button id="mobileSidebarToggle" class="mr-4 text-gray-500 lg:hidden">
                            <i class="fas fa-bars"></i>
                        </button>
                        <h1 class="text-xl font-semibold text-gray-900">Dashboard de Auditoria</h1>
                    </div>
                    <div class="flex items-center space-x-4">
                        <button class="p-2 text-gray-500 hover:text-gray-700">
                            <i class="fas fa-bell"></i>
                        </button>
                        <button class="p-2 text-gray-500 hover:text-gray-700">
                            <i class="fas fa-envelope"></i>
                        </button>
                        <div class="relative">
                            <input type="text" placeholder="Pesquisar..." class="pl-8 pr-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
                            <i class="fas fa-search absolute left-3 top-3 text-gray-400"></i>
                        </div>
                    </div>
                </div>
            </header>

            <!-- Main Content Area -->
            <main class="flex-1 overflow-y-auto p-6 bg-gray-50">
                <!-- Summary Cards -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-sm font-medium text-gray-500">Total de Guias</p>
                                <p class="text-2xl font-bold mt-1">1,248</p>
                            </div>
                            <div class="p-3 rounded-full bg-indigo-100 text-indigo-600">
                                <i class="fas fa-file-invoice text-xl"></i>
                            </div>
                        </div>
                        <div class="mt-4">
                            <span class="text-sm text-green-600 font-medium">
                                <i class="fas fa-arrow-up"></i> 12.5%
                            </span>
                            <span class="text-sm text-gray-500 ml-2">vs último mês</span>
                        </div>
                    </div>
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-sm font-medium text-gray-500">Inconsistências</p>
                                <p class="text-2xl font-bold mt-1">187</p>
                            </div>
                            <div class="p-3 rounded-full bg-red-100 text-red-600">
                                <i class="fas fa-exclamation-triangle text-xl"></i>
                            </div>
                        </div>
                        <div class="mt-4">
                            <span class="text-sm text-red-600 font-medium">
                                <i class="fas fa-arrow-up"></i> 8.3%
                            </span>
                            <span class="text-sm text-gray-500 ml-2">vs último mês</span>
                        </div>
                    </div>
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-sm font-medium text-gray-500">Valor Glosado</p>
                                <p class="text-2xl font-bold mt-1">R$ 24,750</p>
                            </div>
                            <div class="p-3 rounded-full bg-yellow-100 text-yellow-600">
                                <i class="fas fa-money-bill-wave text-xl"></i>
                            </div>
                        </div>
                        <div class="mt-4">
                            <span class="text-sm text-red-600 font-medium">
                                <i class="fas fa-arrow-up"></i> 15.2%
                            </span>
                            <span class="text-sm text-gray-500 ml-2">vs último mês</span>
                        </div>
                    </div>
                    <div class="bg-white rounded-lg shadow p-6">
                        <div class="flex items-center justify-between">
                            <div>
                                <p class="text-sm font-medium text-gray-500">Recuperado</p>
                                <p class="text-2xl font-bold mt-1">R$ 8,420</p>
                            </div>
                            <div class="p-3 rounded-full bg-green-100 text-green-600">
                                <i class="fas fa-hand-holding-usd text-xl"></i>
                            </div>
                        </div>
                        <div class="mt-4">
                            <span class="text-sm text-green-600 font-medium">
                                <i class="fas fa-arrow-up"></i> 22.7%
                            </span>
                            <span class="text-sm text-gray-500 ml-2">vs último mês</span>
                        </div>
                    </div>
                </div>

                <!-- Charts and Data Upload -->
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
                    <!-- Chart 1 -->
                    <div class="bg-white rounded-lg shadow p-6 lg:col-span-2">
                        <div class="flex items-center justify-between mb-4">
                            <h2 class="text-lg font-semibold">Distribuição de Inconsistências</h2>
                            <div class="flex space-x-2">
                                <button class="px-3 py-1 text-sm bg-gray-100 rounded-md hover:bg-gray-200">Mensal</button>
                                <button class="px-3 py-1 text-sm bg-indigo-600 text-white rounded-md hover:bg-indigo-700">Anual</button>
                            </div>
                        </div>
                        <div class="chart-container">
                            <canvas id="inconsistencyChart"></canvas>
                        </div>
                    </div>
                    
                    <!-- Data Upload -->
                    <div class="bg-white rounded-lg shadow p-6">
                        <h2 class="text-lg font-semibold mb-4">Importar Dados</h2>
                        <div class="file-upload rounded-lg p-6 text-center mb-4" id="dropZone">
                            <i class="fas fa-cloud-upload-alt text-4xl text-indigo-500 mb-3"></i>
                            <p class="font-medium">Arraste e solte arquivos aqui</p>
                            <p class="text-sm text-gray-500 mt-1">ou</p>
                            <label for="fileInput" class="mt-3 inline-block px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 cursor-pointer">
                                Selecione arquivos
                            </label>
                            <input type="file" id="fileInput" class="hidden" multiple>
                            <button id="testDataBtn" class="mt-3 w-full px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 flex items-center justify-center">
                                <i class="fas fa-flask mr-2"></i> Testar com Dados Reais
                            </button>
                        </div>
                        <div id="fileList" class="mt-4 hidden">
                            <h4 class="font-medium mb-2">Arquivos Carregados:</h4>
                            <ul id="uploadedFiles" class="space-y-2">
                                <!-- Files will be listed here -->
                            </ul>
                        </div>
                        <div class="text-sm text-gray-500 mt-4">
                            <p>Formatos suportados: PDF, CSV, XLSX</p>
                            <p class="mt-1">Máximo: 10 arquivos por vez</p>
                        </div>
                    </div>
                </div>

                <!-- Inconsistency Types -->
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
                    <div class="bg-white rounded-lg shadow p-4 flex items-center">
                        <div class="p-2 rounded-full bg-red-100 text-red-600 mr-3">
                            <i class="fas fa-exchange-alt"></i>
                        </div>
                        <div>
                            <p class="text-sm font-medium">Divergência Global</p>
                            <p class="text-lg font-bold">42 casos</p>
                        </div>
                    </div>
                    <div class="bg-white rounded-lg shadow p-4 flex items-center">
                        <div class="p-2 rounded-full bg-yellow-100 text-yellow-600 mr-3">
                            <i class="fas fa-percentage"></i>
                        </div>
                        <div>
                            <p class="text-sm font-medium">Discrepância por Guia</p>
                            <p class="text-lg font-bold">65 casos</p>
                        </div>
                    </div>
                    <div class="bg-white rounded-lg shadow p-4 flex items-center">
                        <div class="p-2 rounded-full bg-blue-100 text-blue-600 mr-3">
                            <i class="fas fa-cut"></i>
                        </div>
                        <div>
                            <p class="text-sm font-medium">Pagamento Parcial</p>
                            <p class="text-lg font-bold">38 casos</p>
                        </div>
                    </div>
                    <div class="bg-white rounded-lg shadow p-4 flex items-center">
                        <div class="p-2 rounded-full bg-purple-100 text-purple-600 mr-3">
                            <i class="fas fa-copy"></i>
                        </div>
                        <div>
                            <p class="text-sm font-medium">Duplicidade</p>
                            <p class="text-lg font-bold">12 casos</p>
                        </div>
                    </div>
                </div>

                <!-- Inconsistencies Table -->
                <div class="bg-white rounded-lg shadow overflow-hidden mb-6">
                    <div class="px-6 py-4 border-b flex items-center justify-between">
                        <h2 class="text-lg font-semibold">Inconsistências Detectadas</h2>
                        <div class="flex space-x-2">
                            <div class="relative">
                                <select class="appearance-none bg-gray-100 border border-gray-300 rounded-md pl-3 pr-8 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500">
                                    <option>Todas as Inconsistências</option>
                                    <option>Divergência Global</option>
                                    <option>Discrepância por Guia</option>
                                    <option>Pagamento Parcial</option>
                                    <option>Glosa por Franquia</option>
                                    <option>Guia Não Encontrada</option>
                                    <option>Duplicidade</option>
                                </select>
                                <i class="fas fa-chevron-down absolute right-3 top-3 text-gray-400 pointer-events-none"></i>
                            </div>
                            <button class="px-3 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 text-sm">
                                <i class="fas fa-download mr-1"></i> Exportar
                            </button>
                        </div>
                    </div>
                    <div class="overflow-x-auto">
                        <table class="min-w-full divide-y divide-gray-200">
                            <thead class="bg-gray-50">
                                <tr>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Guia</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Paciente</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Convênio</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Valor Clínica</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Valor Convênio</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Tipo</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                                    <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Ações</th>
                                </tr>
                            </thead>
                            <tbody class="bg-white divide-y divide-gray-200">
                                <tr class="hover:bg-gray-50">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">GU2023-456</div>
                                        <div class="text-sm text-gray-500">15/05/2023</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">Maria Silva</div>
                                        <div class="text-sm text-gray-500">CPF: 123.456.789-00</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">Amil Saúde</div>
                                        <div class="text-sm text-gray-500">Contrato: 789456</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex flex-col">
                                            <span class="font-medium">R$ 1.250,00</span>
                                            <span class="text-sm text-gray-500">Total Faturado</span>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex flex-col">
                                            <span class="font-medium">R$ 980,00</span>
                                            <span class="text-sm text-gray-500">Total Pago</span>
                                            <span class="text-sm text-red-500">Diferença: R$ 270,00</span>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="inconsistency-badge badge-warning">Discrepância por Guia</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="inconsistency-badge badge-neutral">Pendente</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                        <button class="text-indigo-600 hover:text-indigo-900 mr-3">
                                            <i class="fas fa-eye"></i>
                                        </button>
                                        <button class="text-green-600 hover:text-green-900">
                                            <i class="fas fa-check"></i>
                                        </button>
                                    </td>
                                </tr>
                                <tr class="hover:bg-gray-50">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">GU2023-00321</div>
                                        <div class="text-sm text-gray-500">10/05/2023</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">João Oliveira</div>
                                        <div class="text-sm text-gray-500">CPF: 987.654.321-00</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">Unimed</div>
                                        <div class="text-sm text-gray-500">Contrato: 654123</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex flex-col">
                                            <span class="font-medium">R$ 890,00</span>
                                            <span class="text-sm text-gray-500">Pago: R$ 0,00</span>
                                            <span class="text-sm text-red-500">Diferença: R$ 890,00</span>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="inconsistency-badge badge-error">Guia Não Encontrada</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="inconsistency-badge badge-neutral">Pendente</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                        <button class="text-indigo-600 hover:text-indigo-900 mr-3">
                                            <i class="fas fa-eye"></i>
                                        </button>
                                        <button class="text-green-600 hover:text-green-900">
                                            <i class="fas fa-check"></i>
                                        </button>
                                    </td>
                                </tr>
                                <tr class="hover:bg-gray-50">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">GU2023-00289</div>
                                        <div class="text-sm text-gray-500">08/05/2023</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">Ana Costa</div>
                                        <div class="text-sm text-gray-500">CPF: 456.789.123-00</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">Bradesco Saúde</div>
                                        <div class="text-sm text-gray-500">Contrato: 321654</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex flex-col">
                                            <span class="font-medium">R$ 2.150,00</span>
                                            <span class="text-sm text-gray-500">Pago: R$ 1.720,00</span>
                                            <span class="text-sm text-red-500">Diferença: R$ 430,00</span>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="inconsistency-badge badge-info">Glosa por Franquia</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="inconsistency-badge badge-success">Resolvida</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                        <button class="text-indigo-600 hover:text-indigo-900 mr-3">
                                            <i class="fas fa-eye"></i>
                                        </button>
                                        <button class="text-green-600 hover:text-green-900">
                                            <i class="fas fa-check"></i>
                                        </button>
                                    </td>
                                </tr>
                                <tr class="hover:bg-gray-50">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">GU2023-00175</div>
                                        <div class="text-sm text-gray-500">05/05/2023</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">Carlos Mendes</div>
                                        <div class="text-sm text-gray-500">CPF: 789.123.456-00</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">SulAmérica</div>
                                        <div class="text-sm text-gray-500">Contrato: 147258</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex flex-col">
                                            <span class="font-medium">R$ 1.750,00</span>
                                            <span class="text-sm text-gray-500">Pago: R$ 1.750,00</span>
                                            <span class="text-sm text-red-500">Mensagem: Duplicidade</span>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="inconsistency-badge badge-error">Duplicidade</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="inconsistency-badge badge-neutral">Contestada</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                        <button class="text-indigo-600 hover:text-indigo-900 mr-3">
                                            <i class="fas fa-eye"></i>
                                        </button>
                                        <button class="text-green-600 hover:text-green-900">
                                            <i class="fas fa-check"></i>
                                        </button>
                                    </td>
                                </tr>
                                <tr class="hover:bg-gray-50">
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">GU2023-00542</div>
                                        <div class="text-sm text-gray-500">18/05/2023</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">Patrícia Lima</div>
                                        <div class="text-sm text-gray-500">CPF: 321.654.987-00</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="font-medium">NotreDame Intermédica</div>
                                        <div class="text-sm text-gray-500">Contrato: 369258</div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <div class="flex flex-col">
                                            <span class="font-medium">R$ 3.420,00</span>
                                            <span class="text-sm text-gray-500">Pago: R$ 2.900,00</span>
                                            <span class="text-sm text-red-500">Diferença: R$ 520,00</span>
                                        </div>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="inconsistency-badge badge-warning">Pagamento Parcial</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap">
                                        <span class="inconsistency-badge badge-neutral">Pendente</span>
                                    </td>
                                    <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                                        <button class="text-indigo-600 hover:text-indigo-900 mr-3">
                                            <i class="fas fa-eye"></i>
                                        </button>
                                        <button class="text-green-600 hover:text-green-900">
                                            <i class="fas fa-check"></i>
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="px-6 py-4 border-t flex items-center justify-between">
                        <div class="text-sm text-gray-500">
                            Mostrando <span class="font-medium">1</span> a <span class="font-medium">5</span> de <span class="font-medium">187</span> resultados
                        </div>
                        <div class="flex space-x-2">
                            <button class="px-3 py-1 border rounded-md text-sm hover:bg-gray-50">Anterior</button>
                            <button class="px-3 py-1 bg-indigo-600 text-white rounded-md text-sm hover:bg-indigo-700">1</button>
                            <button class="px-3 py-1 border rounded-md text-sm hover:bg-gray-50">2</button>
                            <button class="px-3 py-1 border rounded-md text-sm hover:bg-gray-50">3</button>
                            <button class="px-3 py-1 border rounded-md text-sm hover:bg-gray-50">Próximo</button>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    </div>

    <!-- Modal for Inconsistency Detail -->
    <div id="inconsistencyModal" class="fixed inset-0 z-50 hidden overflow-y-auto">
        <div class="flex items-center justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0">
            <div class="fixed inset-0 transition-opacity" aria-hidden="true">
                <div class="absolute inset-0 bg-gray-500 opacity-75"></div>
            </div>
            <span class="hidden sm:inline-block sm:align-middle sm:h-screen" aria-hidden="true">&#8203;</span>
            <div class="inline-block align-bottom bg-white rounded-lg text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-4xl sm:w-full">
                <div class="bg-white px-4 pt-5 pb-4 sm:p-6 sm:pb-4">
                    <div class="sm:flex sm:items-start">
                        <div class="mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left w-full">
                            <div class="flex justify-between items-center">
                                <h3 class="text-lg leading-6 font-medium text-gray-900" id="modalTitle">
                                    Detalhes da Inconsistência
                                </h3>
                                <button type="button" class="closeModal text-gray-400 hover:text-gray-500">
                                    <i class="fas fa-times"></i>
                                </button>
                            </div>
                            <div class="mt-4">
                                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                                    <div>
                                        <h4 class="font-medium text-gray-700 mb-2">Informações da Guia</h4>
                                        <div class="bg-gray-50 p-4 rounded-lg">
                                            <div class="grid grid-cols-2 gap-2">
                                                <div>
                                                    <p class="text-sm text-gray-500">Número da Guia:</p>
                                                    <p class="font-medium">GU2023-00456</p>
                                                </div>
                                                <div>
                                                    <p class="text-sm text-gray-500">Data do Atendimento:</p>
                                                    <p class="font-medium">15/05/2023</p>
                                                </div>
                                                <div>
                                                    <p class="text-sm text-gray-500">Paciente:</p>
                                                    <p class="font-medium">Maria Silva</p>
                                                </div>
                                                <div>
                                                    <p class="text-sm text-gray-500">Convênio:</p>
                                                    <p class="font-medium">Amil Saúde</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div>
                                        <h4 class="font-medium text-gray-700 mb-2">Valores</h4>
                                        <div class="bg-gray-50 p-4 rounded-lg">
                                            <div class="grid grid-cols-2 gap-2">
                                                <div>
                                                    <p class="text-sm text-gray-500">Valor Clínica:</p>
                                                    <p class="font-medium">R$ 1.250,00</p>
                                                    <p class="text-xs text-gray-400">Total Faturado</p>
                                                </div>
                                                <div>
                                                    <p class="text-sm text-gray-500">Valor Convênio:</p>
                                                    <p class="font-medium">R$ 980,00</p>
                                                    <p class="text-xs text-gray-400">Total Pago</p>
                                                </div>
                                                <div>
                                                    <p class="text-sm text-gray-500">Diferença:</p>
                                                    <p class="font-medium text-red-600">R$ 270,00</p>
                                                </div>
                                                <div>
                                                    <p class="text-sm text-gray-500">Franquia:</p>
                                                    <p class="font-medium">R$ 0,00</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div class="mb-6">
                                    <h4 class="font-medium text-gray-700 mb-2">Procedimentos</h4>
                                    <div class="overflow-x-auto">
                                        <table class="min-w-full divide-y divide-gray-200">
                                            <thead class="bg-gray-50">
                                                <tr>
                                                    <th scope="col" class="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Código</th>
                                                    <th scope="col" class="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Descrição</th>
                                                    <th scope="col" class="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Valor Informado</th>
                                                    <th scope="col" class="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Valor Pago</th>
                                                    <th scope="col" class="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Franquia</th>
                                                    <th scope="col" class="px-3 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                                                </tr>
                                            </thead>
                                            <tbody class="bg-white divide-y divide-gray-200">
                                                <tr>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">40901234</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">Consulta Médica</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">R$ 350,00</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">R$ 350,00</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">R$ 0,00</td>
                                                    <td class="px-3 py-2 whitespace-nowrap">
                                                        <span class="inconsistency-badge badge-success">Pago</span>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">40301245</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">Eletrocardiograma</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">R$ 450,00</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">R$ 450,00</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">R$ 0,00</td>
                                                    <td class="px-3 py-2 whitespace-nowrap">
                                                        <span class="inconsistency-badge badge-success">Pago</span>
                                                    </td>
                                                </tr>
                                                <tr>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">42101256</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">Ecocardiograma</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">R$ 450,00</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">R$ 180,00</td>
                                                    <td class="px-3 py-2 whitespace-nowrap text-sm">R$ 0,00</td>
                                                    <td class="px-3 py-2 whitespace-nowrap">
                                                        <span class="inconsistency-badge badge-warning">Glosa Parcial</span>
                                                    </td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                                
                                <div class="mb-4">
                                    <h4 class="font-medium text-gray-700 mb-2">Mensagens de Glosa</h4>
                                    <div class="bg-yellow-50 border-l-4 border-yellow-400 p-4">
                                        <div class="flex">
                                            <div class="flex-shrink-0">
                                                <i class="fas fa-exclamation-triangle text-yellow-400"></i>
                                            </div>
                                            <div class="ml-3">
                                                <p class="text-sm text-yellow-700">
                                                    <span class="font-medium">Atenção!</span> Procedimento 42101256 - Ecocardiograma teve valor glosado parcialmente (R$ 270,00) com a mensagem: "Valor acima da tabela do convênio".
                                                </p>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                
                                <div>
                                    <h4 class="font-medium text-gray-700 mb-2">Ações</h4>
                                    <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                                        <button class="px-4 py-2 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 text-sm flex items-center justify-center">
                                            <i class="fas fa-file-pdf mr-2"></i> Gerar Contestação
                                        </button>
                                        <button class="px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 text-sm flex items-center justify-center">
                                            <i class="fas fa-check-circle mr-2"></i> Marcar como Resolvida
                                        </button>
                                        <button class="px-4 py-2 bg-gray-200 text-gray-700 rounded-md hover:bg-gray-300 text-sm flex items-center justify-center">
                                            <i class="fas fa-times-circle mr-2"></i> Descartar
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="bg-gray-50 px-4 py-3 sm:px-6 sm:flex sm:flex-row-reverse">
                    <button type="button" class="closeModal mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 sm:mt-0 sm:ml-3 sm:w-auto sm:text-sm">
                        Fechar
                    </button>
                </div>
            </div>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script>
        // Sidebar toggle
        const sidebar = document.querySelector('.sidebar');
        const mainContent = document.querySelector('.main-content');
        const sidebarCollapse = document.getElementById('sidebarCollapse');
        const mobileSidebarToggle = document.getElementById('mobileSidebarToggle');
        
        sidebarCollapse.addEventListener('click', () => {
            sidebar.classList.toggle('collapsed');
        });
        
        mobileSidebarToggle.addEventListener('click', () => {
            sidebar.classList.toggle('open');
        });

        // File upload drag and drop
        const dropZone = document.getElementById('dropZone');
        const fileInput = document.getElementById('fileInput');
        
        dropZone.addEventListener('click', () => {
            fileInput.click();
        });
        
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, preventDefaults, false);
        });
        
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }
        
        ['dragenter', 'dragover'].forEach(eventName => {
            dropZone.addEventListener(eventName, highlight, false);
        });
        
        ['dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, unhighlight, false);
        });
        
        function highlight() {
            dropZone.classList.add('dragover');
        }
        
        function unhighlight() {
            dropZone.classList.remove('dragover');
        }
        
        dropZone.addEventListener('drop', handleDrop, false);
        
        function handleDrop(e) {
            const dt = e.dataTransfer;
            const files = dt.files;
            handleFiles(files);
        }
        
        fileInput.addEventListener('change', function() {
            handleFiles(this.files);
        });
        
        function handleFiles(files) {
            if (files.length > 10) {
                alert('Máximo de 10 arquivos permitidos.');
                return;
            }
            
            const fileList = document.getElementById('fileList');
            const uploadedFilesList = document.getElementById('uploadedFiles');
            
            // Clear previous files
            uploadedFilesList.innerHTML = '';
            
            // Add new files to the list
            Array.from(files).forEach(file => {
                const listItem = document.createElement('li');
                listItem.className = 'flex items-center justify-between bg-gray-50 p-2 rounded';
                
                const fileInfo = document.createElement('div');
                fileInfo.className = 'flex items-center';
                
                const icon = document.createElement('i');
                icon.className = 'fas fa-file text-gray-500 mr-2';
                
                const fileName = document.createElement('span');
                fileName.className = 'text-sm';
                fileName.textContent = file.name;
                
                const fileSize = document.createElement('span');
                fileSize.className = 'text-xs text-gray-500 ml-2';
                fileSize.textContent = `(${(file.size / 1024).toFixed(2)} KB)`;
                
                const statusBadge = document.createElement('span');
                statusBadge.className = 'text-xs bg-green-100 text-green-800 px-2 py-1 rounded';
                statusBadge.textContent = 'Pronto para análise';
                
                fileInfo.appendChild(icon);
                fileInfo.appendChild(fileName);
                fileInfo.appendChild(fileSize);
                
                listItem.appendChild(fileInfo);
                listItem.appendChild(statusBadge);
                
                uploadedFilesList.appendChild(listItem);
            });
            
            fileList.classList.remove('hidden');
            
            // Here you would process the files (upload, parse, etc.)
            console.log('Files selected:', files);
        }

        // Test data button functionality
        const testDataBtn = document.getElementById('testDataBtn');
        testDataBtn.addEventListener('click', () => {
            if(confirm('Deseja carregar dados de teste para demonstrar o sistema?\nIsso irá simular uma importação real.')) {
                // Simulate processing
                setTimeout(() => {
                    // Update dashboard numbers
                    document.querySelectorAll('.bg-white.rounded-lg.shadow.p-6')[0].querySelector('p.text-2xl').textContent = '2,543';
                    document.querySelectorAll('.bg-white.rounded-lg.shadow.p-6')[1].querySelector('p.text-2xl').textContent = '326';
                    document.querySelectorAll('.bg-white.rounded-lg.shadow.p-6')[2].querySelector('p.text-2xl').textContent = 'R$ 48,920';
                    document.querySelectorAll('.bg-white.rounded-lg.shadow.p-6')[3].querySelector('p.text-2xl').textContent = 'R$ 15,780';
                    
                    // Update chart
                    inconsistencyChart.data.datasets[0].data = [87, 132, 65, 42, 18, 12];
                    inconsistencyChart.update();
                    
                    alert('Dados de teste carregados com sucesso!\nO dashboard foi atualizado com informações simuladas.');
                }, 1500);
            }
        });

        // Modal functionality
        const modal = document.getElementById('inconsistencyModal');
        const closeButtons = document.querySelectorAll('.closeModal');
        const viewButtons = document.querySelectorAll('button:has(.fa-eye)');
        
        viewButtons.forEach(button => {
            button.addEventListener('click', () => {
                modal.classList.remove('hidden');
            });
        });
        
        closeButtons.forEach(button => {
            button.addEventListener('click', () => {
                modal.classList.add('hidden');
            });
        });

        // Chart initialization
        const ctx = document.getElementById('inconsistencyChart').getContext('2d');
        const inconsistencyChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Divergência Global', 'Discrepância por Guia', 'Pagamento Parcial', 'Glosa por Franquia', 'Guia Não Encontrada', 'Duplicidade'],
                datasets: [{
                    label: 'Inconsistências por Tipo',
                    data: [42, 65, 38, 27, 12, 9],
                    backgroundColor: [
                        'rgba(239, 68, 68, 0.7)',
                        'rgba(249, 115, 22, 0.7)',
                        'rgba(59, 130, 246, 0.7)',
                        'rgba(139, 92, 246, 0.7)',
                        'rgba(75, 85, 99, 0.7)',
                        'rgba(220, 38, 38, 0.7)'
                    ],
                    borderColor: [
                        'rgba(239, 68, 68, 1)',
                        'rgba(249, 115, 22, 1)',
                        'rgba(59, 130, 246, 1)',
                        'rgba(139, 92, 246, 1)',
                        'rgba(75, 85, 99, 1)',
                        'rgba(220, 38, 38, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    </script>
</body>
</html>
