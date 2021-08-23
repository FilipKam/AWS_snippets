import * as cdk from '@aws-cdk/core';
import ssm=require('@aws-cdk/aws-ssm');

export class SsmStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
   

  const patchFilterProductWindowsServer = {
    key: 'PRODUCT',
    values: ['WindowsServer2019']
};

const patchFilterClassificationWindowsServer = {
    key: 'CLASSIFICATION',
    values: [
        'CriticalUpdates',
        'SecurityUpdates',
        'Updates'
    ]
};

const patchFilterSeverityWindowsServer = {
    key: 'MSRC_SEVERITY',
    values: [
        'Critical',
        'Important'
    ]
};

const patchBaselinePatchFilterGroupWindowsServer = {
    patchFilters: [
      patchFilterProductWindowsServer,
        patchFilterClassificationWindowsServer,
        patchFilterSeverityWindowsServer
    ]
};

const patchBaselineRuleHighWindowsServer = {
    approveAfterDays: 7,
    complianceLevel: "HIGH",
    patchFilterGroup: patchBaselinePatchFilterGroupWindowsServer
};

const patchFilterProductWindowsServerSQL = {
  key: 'PRODUCT_FAMILY',
  values: ['SQL Server']
};


const patchFilterPatchSet = {
  key: 'PATCH_SET',
  values: ['APPLICATION']
};

const patchBaselinePatchFilterGroupWindowsServerSql = {
  patchFilters: [
      patchFilterProductWindowsServerSQL,
      patchFilterPatchSet
  ]
};

const patchBaselineRuleHighWindowsServerSql = {
  approveAfterDays: 7,
  complianceLevel: "HIGH",
  patchFilterGroup: patchBaselinePatchFilterGroupWindowsServerSql
};

const patchBaselineRuleGroupWindowsServer = {
    patchRules: [
        patchBaselineRuleHighWindowsServer,
        patchBaselineRuleHighWindowsServerSql
    ]
};

const patchBaselineWinServer = new ssm.CfnPatchBaseline(this, "Windows-Server-CritImp-CDK", {
    name: "Windows-Server-CritImp-CDK",
    operatingSystem: "WINDOWS",
    patchGroups:[ "Windows-Server-CDK"],
    approvalRules: patchBaselineRuleGroupWindowsServer
});

  }
}
